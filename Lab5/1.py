import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def first_task():
    x = 1.5

    first_part = np.power(np.sin(np.pi / 2 + 1))
    second_part = x * np.power(3 + np.power(x, 2), 1./4.)
    third_part = np.power(np.tan(np.power(x, 3) - 1), 3)
    fourth_part = np.arctan(x / 2) - np.log(17.56)

    answer = (first_part + second_part - third_part) / fourth_part

    print(f"\n\tAnswer to the Calculated Expression - {answer}")

    X = np.column_stack((np.ones(12), np.arange(2, 14), np.random.randint(60, 83, 12)))
    Y = np.random.uniform(13.5, 18.6, 12)

    XT = X.T
    XTX_inverse = np.linalg.inv(np.dot(XT, X))
    XTY = np.dot(XT, Y)
    A = np.dot(XTX_inverse, XTY)

    print(f"\n\tSignificance of Regression Coefficients:"
          f"\n\ta0 = {A[0]}"
          f"\n\ta1 = {A[1]}"
          f"\n\ta2 = {A[2]}")

    Y_rough = A[0] + A[1] * X[:, 1] + A[2] * X[:, 2]

    print(f"\n\tInitial Y Value: {Y}"
          f"\n\tReceived Y Value: {Y_rough}")


def second_task():
    df = pd.read_csv('test.csv')

    df = df.sample(n=1000)

    print(f"\n\tData Omissions\n{df.isnull().sum()}")

    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)

    df['Square'].plot(kind='box', logy=True)
    
    plt.title('Boxplot with Logarithmic Scale')

    plt.subplot(1, 2, 2)

    df['Square'].plot(kind='hist', bins=30, logy=True)

    plt.title('Histogram with Logarithmic Scale')

    plt.show()

    numeric_columns = ['Square', 'LifeSquare', 'KitchenSquare', 'Healthcare_1']

    df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

    df = df[(df['Square'] > 20) & (df['Square'] < 200)]

    print(f"\n\tNumber of Apartments by Number of Rooms \n{df['Rooms'].value_counts()}")

    pivot_table = df.pivot_table(index='DistrictId', columns='Rooms', values='Id', aggfunc='count')

    print(f"\n\tSummary Table \n{pivot_table}")

    df.to_csv('surname.csv', index=False)


def third_task():
    x = 1.21

    a_values = np.arange(3.5, 25.5, 1.5)
    
    f_values = []

    for a in a_values:
        f = np.arcsin(x / 3) + 1.2 * a
        f_values.append(f)

    f_max = max(f_values)
    f_min = min(f_values)
    f_avg = np.mean(f_values)
    f_len = len(f_values)

    plt.plot(a_values, f_values, label="F(x)")

    line_avg = [f_avg] * len(a_values)
    plt.plot(a_values, line_avg, label="Average Value", linestyle='solid')

    plt.xlabel("a")
    plt.ylabel("F(x)")
    plt.title("Graph of Function F(x)")
    plt.legend()

    plt.show()

    x = np.linspace(0, 10, 100)
    y = np.linspace(0, 10, 100)
    X, Y = np.meshgrid(x, y)

    Z1 = np.power(X, 0.25) + np.power(Y, 0.25)
    Z2 = np.power(X, 2) - np.power(Y, 2)
    Z3 = 2 * X + 3 * Y
    Z4 = np.power(X, 2) + np.power(Y, 2)
    Z5 = 2 + 2 * X + 2 * Y - np.power(X, 2) - np.power(Y, 2)

    ax = plt.figure(figsize=(15, 15))

    ax1 = ax.add_subplot(321, projection='3d')
    ax1.plot_surface(X, Y, Z1, cmap='viridis')
    ax1.set_title('Z1')

    ax2 = ax.add_subplot(322, projection='3d')
    ax2.plot_surface(X, Y, Z2, cmap='viridis')
    ax2.set_title('Z2')

    ax3 = ax.add_subplot(323, projection='3d')
    ax3.plot_surface(X, Y, Z3, cmap='viridis')
    ax3.set_title('Z3')

    ax4 = ax.add_subplot(324, projection='3d')
    ax4.plot_surface(X, Y, Z4, cmap='viridis')
    ax4.set_title('Z4')

    ax5 = ax.add_subplot(325, projection='3d')
    ax5.plot_surface(X, Y, Z5, cmap='viridis')
    ax5.set_title('Z5')

    plt.tight_layout()
    plt.show()


def menu():
    print("\n\tHello, Dear User!")

    while True:

        print("\n\tMenu:"
              "\n\t1. First Task"
              "\n\t2. Second Task"
              "\n\t3. Third Task"
              "\n\t4. Fourth Task"
              "\n\tAnother. Exit")

        choice = input("\n\tInput Number of Task from Menu to Test: ")

        if choice == "1":
            first_task()

        elif choice == "2":
            second_task()

        elif choice == "3":
            third_task()

        else:
            print("\n\tGoodbye, Dear User!")
            break