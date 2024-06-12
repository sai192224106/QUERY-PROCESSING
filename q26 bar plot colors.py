import matplotlib.pyplot as plt

# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8.0, 7.7, 6.7]

plt.figure(figsize=(10, 6))
#bar is used along with 'h' for horinzatal bar graph
plt.bar(languages, popularity, color=['blue', 'green', 'red', 'orange', 'purple', 'cyan'])
plt.title('Popularity of Programming Languages')
plt.xlabel('Popularity (%)')
plt.ylabel('Programming Languages')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()