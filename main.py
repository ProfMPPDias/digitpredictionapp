import tkinter as tk
from tkinter import messagebox
from sklearn.datasets import fetch_openml
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageOps
import warnings

# Suprimir erros
warnings.filterwarnings("ignore", category=UserWarning, module='sklearn')

# Carregar o conjunto de dados MNIST
mnist = fetch_openml('mnist_784', version=1)
X, y = mnist.data, mnist.target.astype(int)

# Dividir os dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar um modelo de Machine Learning
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)

# Avaliação do modelo
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy * 100:.2f}%")

# Função para prever o número desenhado
def predict_digit(image):
    image = image.resize((28, 28)).convert('L')
    image = ImageOps.invert(image)
    image = np.array(image).reshape(1, -1)
    prediction = clf.predict(image)
    return prediction[0]

class DrawApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Desenhe um Número")
        self.canvas = tk.Canvas(self.master, width=200, height=200, bg='white')
        self.canvas.grid(row=0, column=0, columnspan=10)
        self.canvas.bind("<B1-Motion>", self.paint)
        
        self.button_predict = tk.Button(self.master, text="Prever", command=self.predict)
        self.button_predict.grid(row=1, column=0, columnspan=10)

        self.leds = []
        for i in range(10):
            led = tk.Label(self.master, text=str(i), bg='red', width=5)
            led.grid(row=2, column=i)
            self.leds.append(led)

        self.image = Image.new('RGB', (200, 200), 'white')
        self.draw = ImageDraw.Draw(self.image)

    def paint(self, event):
        x1, y1 = (event.x - 2), (event.y - 2)
        x2, y2 = (event.x + 2), (event.y + 2)
        self.canvas.create_oval(x1, y1, x2, y2, fill='black', width=5)
        self.draw.ellipse([x1, y1, x2, y2], fill='black')

    def predict(self):
        digit = predict_digit(self.image)
        for i, led in enumerate(self.leds):
            if i == digit:
                led.config(bg='green')
            else:
                led.config(bg='red')
        messagebox.showinfo("Previsão", f"O número desenhado foi: {digit}")
        self.image = Image.new('RGB', (200, 200), 'white')
        self.draw = ImageDraw.Draw(self.image)
        self.canvas.delete("all")

if __name__ == '__main__':
    root = tk.Tk()
    app = DrawApp(root)
    root.mainloop()