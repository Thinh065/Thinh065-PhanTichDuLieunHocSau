import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Tạo DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ivan", "Jack", "Kelly", "Liam", "Mona", "Nina", "Oscar"],
    "Age": [25, 30, 35, 28, 22, 45, 34, 31, 27, 29, 33, 40, 26, 32, 36],
    "Salary": [50000, 60000, 70000, 55000, 52000, 80000, 72000, 68000, 61000, 59000, 63000, 77000, 53000, 66000, 75000]
}
df = pd.DataFrame(data)

# 2. Hiển thị thông tin DataFrame
print(df.info())

# 3. Lọc các hàng có 'Age' lớn hơn 28
filtered_df = df[df['Age'] > 28]
print(filtered_df)

# 4. Tính giá trị trung bình của cột 'Salary'
mean_salary = df['Salary'].mean()
print("Mean Salary:", mean_salary)

# 5. Nhóm dữ liệu theo 'Age' và tính tổng 'Salary'
grouped_salary = df.groupby('Age')['Salary'].sum()
print(grouped_salary)

# 6. Sắp xếp DataFrame theo cột 'Salary' giảm dần
sorted_df = df.sort_values(by='Salary', ascending=False)
print(sorted_df)

# 7. Vẽ biểu đồ cột cho cột 'Age'
df['Age'].value_counts().plot(kind='bar')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# 8. Vẽ biểu đồ đường cho cột 'Salary'
df['Salary'].plot(kind='line', marker='o')
plt.title("Salary Trend")
plt.xlabel("Index")
plt.ylabel("Salary")
plt.show()

# 9. Vẽ biểu đồ tròn cho cột 'Age'
df['Age'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Age Distribution")
plt.show()

# 10. Vẽ biểu đồ phân tán cho 'Age' và 'Salary'
plt.scatter(df['Age'], df['Salary'])
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()

# 11. Kiểm tra giá trị NaN
print(df.isnull().sum())

# 12. Thay thế 'Age' > 30 bằng giá trị trung bình của cột
mean_age = df['Age'].mean()
df.loc[df['Age'] > 30, 'Age'] = mean_age
print(df)

# 13. Chuẩn hóa cột 'Age'
df['Age_normalized'] = (df['Age'] - df['Age'].min()) / (df['Age'].max() - df['Age'].min())
print(df)

# 14. Phân loại nhóm tuổi
def age_category(age):
    if age < 30:
        return "Young"
    elif 30 <= age < 40:
        return "Middle-aged"
    else:
        return "Old"
df['Age_group'] = df['Age'].apply(age_category)
print(df)

# 15. Tính tỷ lệ phần trăm thay đổi của 'Salary'
df['Salary_pct_change'] = df['Salary'].pct_change() * 100
print(df)

# 16. Tìm và loại bỏ giá trị trùng lặp trên 'Name'
df.drop_duplicates(subset=['Name'], keep='first', inplace=True)
print(df)
