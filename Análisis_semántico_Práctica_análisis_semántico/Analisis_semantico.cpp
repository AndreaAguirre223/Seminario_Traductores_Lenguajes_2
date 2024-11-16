#include <iostream>
#include <unordered_map>
#include <string>
#include <memory>

// Clase base para la representaci�n de variables
class DefVar {
public:
    std::string tipo;

    DefVar(const std::string& t) : tipo(t) {}
};

// Clase para manejar la tabla de s�mbolos
class TablaSimbolos {
private:
    std::unordered_map<std::string, std::shared_ptr<DefVar>> tabla;
public:
    // M�todo para agregar variables a la tabla de s�mbolos
    void agrega(const std::string& nombre, const std::string& tipo) {
        if (tabla.find(nombre) == tabla.end()) {
            tabla[nombre] = std::make_shared<DefVar>(tipo);
            std::cout << "\033[1;32mVariable '" << nombre << "' agregada a la tabla.\033[0m" << std::endl;
        } else {
            std::cout << "\033[1;31mError: simbolo '" << nombre << "' ya definido en el ambito.\033[0m" << std::endl;
        }
    }

    // M�todo para validar los tipos de las variables en la tabla
    void validaTipos() {
        std::cout << "\033[1;34mValidando tipos para las variables:\033[0m" << std::endl;
        for (const auto& entry : tabla) {
            std::cout << "  \033[1;33mValidando tipo para la variable: \033[0m" << entry.first
                      << " \033[1;36mde tipo " << entry.second->tipo << "\033[0m" << std::endl;
        }

        std::cout << "\n\033[1;35mContenido de la tabla de simbolos:\033[0m" << std::endl;
        for (const auto& entry : tabla) {
            std::cout << "  \033[1;37mNombre: \033[1;32m" << entry.first
                      << "\033[0m, \033[1;37mTipo: \033[1;36m" << entry.second->tipo << "\033[0m" << std::endl;
        }
    }
};

// Clase base para las expresiones
class Expresion {
public:
    virtual void validaTipos() = 0; // M�todo abstracto para validar los tipos de las expresiones
    virtual ~Expresion() = default;
};

// Clase para la operaci�n de suma (hereda de Expresion)
class Suma : public Expresion {
private:
    std::shared_ptr<DefVar> var1, var2;

public:
    Suma(std::shared_ptr<DefVar> v1, std::shared_ptr<DefVar> v2) : var1(v1), var2(v2) {}

    // Validaci�n de tipos para la operaci�n de suma
    void validaTipos() override {
        std::cout << "\033[1;34mValidando tipos para la operacion de suma:\033[0m" << std::endl;
        if (var1->tipo == var2->tipo) {
            std::cout << "\033[1;32mTipos compatibles: \033[1;36m" << var1->tipo << " + " << var2->tipo << "\033[0m" << std::endl;
        } else {
            std::cout << "\033[1;31mError: tipos incompatibles para la suma: \033[0m"
                      << var1->tipo << " y " << var2->tipo << std::endl;
        }
    }
};

// Clase para la operaci�n de resta (hereda de Expresion)
class Resta : public Expresion {
private:
    std::shared_ptr<DefVar> var1, var2;

public:
    Resta(std::shared_ptr<DefVar> v1, std::shared_ptr<DefVar> v2) : var1(v1), var2(v2) {}

    // Validaci�n de tipos para la operaci�n de resta
    void validaTipos() override {
        std::cout << "\033[1;34mValidando tipos para la operacion de resta:\033[0m" << std::endl;
        if (var1->tipo == var2->tipo) {
            std::cout << "\033[1;32mTipos compatibles: \033[1;36m" << var1->tipo << " - " << var2->tipo << "\033[0m" << std::endl;
        } else {
            std::cout << "\033[1;31mError: tipos incompatibles para la resta: \033[0m"
                      << var1->tipo << " y " << var2->tipo << std::endl;
        }
    }
};

int main() {
    // Crear la tabla de s�mbolos
    TablaSimbolos tabla;

    // Agregar variables a la tabla
    std::cout << "\033[1;34mAgregando variables...\033[0m" << std::endl;
    tabla.agrega("x", "int");
    tabla.agrega("y", "float");
    tabla.agrega("z", "double");

    // Intentar agregar variables repetidas
    std::cout << "\033[1;34mIntentando agregar nuevamente las variables...\033[0m" << std::endl;
    tabla.agrega("x", "int");  // Error, ya definida
    tabla.agrega("y", "float");  // Error, ya definida

    // Validar tipos de las variables en la tabla
    tabla.validaTipos();

    // Crear expresiones de operaciones
    auto varX = std::make_shared<DefVar>("int");
    auto varY = std::make_shared<DefVar>("float");

    // Operaci�n de suma entre dos variables
    std::cout << "\n\033[1;34mOperacion de Suma...\033[0m" << std::endl;
    Suma suma(varX, varY);
    suma.validaTipos();

    // Operaci�n de resta entre dos variables
    std::cout << "\n\033[1;34mOperacion de Resta...\033[0m" << std::endl;
    Resta resta(varX, varY);
    resta.validaTipos();

    return 0;
}



