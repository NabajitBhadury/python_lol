import matplotlib.pyplot as plt

parties = ['ABC', 'XYZ', 'MNP']

votes = [180, 200, 20]

plt.bar(parties, votes, width=0.3)
plt.xlabel('parties')
plt.ylabel('Votes')
plt.title('Vote count')
plt.show()
