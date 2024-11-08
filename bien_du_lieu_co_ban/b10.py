from shapely.geometry import Polygon
import sys

# Đọc input
n = int(input())
triangles = []

for _ in range(n):
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    # Tạo tam giác dưới dạng Polygon từ 3 đỉnh
    triangle = Polygon([(x1, y1), (x2, y2), (x3, y3)])
    triangles.append(triangle)

# Tính diện tích union của tất cả tam giác
union_area = triangles[0]
for triangle in triangles[1:]:
    union_area = union_area.union(triangle)

# In kết quả với độ chính xác 6 chữ số
print(f"{union_area.area:.6f}")

# 3
# 1 1 5 1 3 3
# 1 2 5 2 5 6
# 1 6 5 2 1 2