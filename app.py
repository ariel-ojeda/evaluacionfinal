from flask import Flask, render_template, request

app = Flask(__name__)

# Página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ejercicio 1: Calcular precio con descuento
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])

        # Cálculos
        precio_unitario = 9000
        total_sin_descuento = tarros * precio_unitario  # Calcular total sin descuento
        descuento = 0

        # Definir descuento según la edad
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25

        total_descuento = int(total_sin_descuento * descuento)  # Sin decimales
        total_con_descuento = int(total_sin_descuento - total_descuento)  # Sin decimales

        return render_template('formulario1.html',
                               nombre=nombre,
                               edad=edad,
                               tarros=tarros,
                               total_sin_descuento=total_sin_descuento,  # Pasar total sin descuento al template
                               total_descuento=total_descuento,
                               total_con_descuento=total_con_descuento)

    return render_template('formulario1.html')

# Ejercicio 2: Validación de usuarios
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    usuarios = {'juan': 'admin', 'pepe': 'user'}

    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']

        if usuario in usuarios and usuarios[usuario] == password:
            if usuario == 'juan':
                mensaje = f'Bienvenido administrador {usuario}'
            else:
                mensaje = f'Bienvenido usuario {usuario}'
        else:
            mensaje = 'Usuario o contraseña incorrectos'

        return render_template('formulario2.html', mensaje=mensaje)

    return render_template('formulario2.html')

if __name__ == '__main__':
    app.run(debug=True)
