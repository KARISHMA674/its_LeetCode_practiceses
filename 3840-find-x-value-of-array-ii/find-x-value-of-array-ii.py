class Solution(object):
    def resultArray(self, nums, k, queries):
        """
        :type nums: List[int]
        :type k: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        tree_size = 4 * n
        
        prod = [1] * tree_size
        prefix_cnt = [[0] * k for _ in range(tree_size)]

        def merge_nodes(l_prod, l_cnt, r_prod, r_cnt):
            p = (l_prod * r_prod) % k
            cnt = list(l_cnt)
            for r in range(k):
                if r_cnt[r]:
                    cnt[(l_prod * r) % k] += r_cnt[r]
            return p, cnt

        def pull(node, left_child, right_child):
            prod[node], prefix_cnt[node] = merge_nodes(
                prod[left_child], prefix_cnt[left_child],
                prod[right_child], prefix_cnt[right_child]
            )

        def build(node, l, r):
            if l == r:
                rem = nums[l] % k
                prod[node] = rem
                prefix_cnt[node][rem] = 1
                return

            mid = (l + r) // 2
            left_child = 2 * node
            right_child = 2 * node + 1
            build(left_child, l, mid)
            build(right_child, mid + 1, r)
            pull(node, left_child, right_child)

        def update(node, l, r, idx, val):
            if l == r:
                rem = val % k
                prod[node] = rem
                for m in range(k):
                    prefix_cnt[node][m] = 0
                prefix_cnt[node][rem] = 1
                return

            mid = (l + r) // 2
            left_child = 2 * node
            right_child = 2 * node + 1
            if idx <= mid:
                update(left_child, l, mid, idx, val)
            else:
                update(right_child, mid + 1, r, idx, val)
            pull(node, left_child, right_child)

        def query_range(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return prod[node], prefix_cnt[node]

            mid = (l + r) // 2
            left_child = 2 * node
            right_child = 2 * node + 1

            if qr <= mid:
                return query_range(left_child, l, mid, ql, qr)
            if ql > mid:
                return query_range(right_child, mid + 1, r, ql, qr)

            lp, lcnt = query_range(left_child, l, mid, ql, qr)
            rp, rcnt = query_range(right_child, mid + 1, r, ql, qr)
            return merge_nodes(lp, lcnt, rp, rcnt)

        build(1, 0, n - 1)

        ans = []
        for idx, val, start, x in queries:
            update(1, 0, n - 1, idx, val)
            _, cnt = query_range(1, 0, n - 1, start, n - 1)
            ans.append(cnt[x] if 0 <= x < k else 0)

        return ans