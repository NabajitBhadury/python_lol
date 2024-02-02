
import matplotlib.pyplot as plt


months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
electricity_consumption = [100, 120, 110, 105,
                           130, 125, 140, 135, 150, 145, 155, 160]

plt.bar(months, electricity_consumption, color='skyblue')
plt.xlabel('Month')
plt.ylabel('Electricity Consumption')
plt.title('Electricity Consumption Over 12 Months')
plt.xticks(rotation=45)
plt.show()


# Example data (replace this with your actual data)
