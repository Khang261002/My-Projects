#include <iostream>

class Complex {
    double m_real {0.0};
    double m_imag {0.0};
public:
    Complex() = default;
    Complex(double real, double imag);
    double getReal() const;
    void setReal(double value);
    double getImag() const;
    void setImag(double value);
    double getMagnitude() const;
    Complex getConjugate() const;
    void print() const;

    // friend functions have access to private members
    friend Complex mul(Complex const & c1, Complex const & c2);
    friend Complex div(Complex const & c1, Complex const & c2);

    friend Complex operator+(Complex const & c1, Complex const & c2);
    friend Complex operator-(Complex const & c1, Complex const & c2);
    friend Complex operator*(Complex const & c1, Complex const & c2);
    friend Complex operator/(Complex const & c1, Complex const & c2);
    friend bool operator==(Complex const & c1, Complex const & c2);
};

Complex::Complex(double real, double imag)
: m_real(real), m_imag(imag) {}

double Complex::getReal() const {
    return m_real;
}

void Complex::setReal(double value) {
    m_real = value;
}

double Complex::getImag() const {
    return m_imag;
}

void Complex::setImag(double value) {
    m_imag = value;
}

double Complex::getMagnitude() const {
    return (m_real * m_real) + (m_imag * m_imag);
}

Complex Complex::getConjugate() const {
    Complex result(m_real, -m_imag);
    return result;
}

void Complex::print() const {
    std::cout << m_real << ((m_imag >= 0) ? " +" : " ") << m_imag << "i\n";
}

Complex add(Complex const & c1, Complex const & c2) {
    Complex result(c1.getReal() + c2.getReal(), c1.getImag() + c2.getImag());
    return result;
}

Complex subs(Complex const & c1, Complex const & c2) {
    Complex result(c1.getReal() - c2.getReal(), c1.getImag() - c2.getImag());
    return result;
}

Complex mul(Complex const & c1, Complex const & c2) {
    return Complex ((c1.m_real * c2.m_real) - (c1.m_imag * c2.m_imag), (c1.m_real * c2.m_imag) + (c1.m_imag * c2.m_real));
}

Complex div(Complex const & c1, Complex const & c2) {
    if (c2.m_real == 0 && c2.m_imag == 0) return c2;
    else {
        Complex result = mul(c1, c2.getConjugate());
        double mag = c2.getMagnitude();
        return Complex(result.getReal() / mag, result.getImag() / mag);
    }
}

Complex operator+(Complex const & c1, Complex const & c2) {
    Complex result(c1.m_real + c2.m_real, c1.m_imag + c2.m_imag);
    return result;
}

Complex operator-(Complex const & c1, Complex const & c2) {
    Complex result(c1.m_real - c2.m_real, c1.m_imag - c2.m_imag);
    return result;
}

Complex operator*(Complex const & c1, Complex const & c2) {
    return Complex ((c1.m_real * c2.m_real) - (c1.m_imag * c2.m_imag), (c1.m_real * c2.m_imag) + (c1.m_imag * c2.m_real));
}

Complex operator/(Complex const & c1, Complex const & c2) {
    if (c2.m_real == 0 && c2.m_imag == 0) return c2;
    else {
        Complex result = mul(c1, c2.getConjugate());
        double mag = c2.getMagnitude();
        return Complex(result.getReal() / mag, result.getImag() / mag);
    }
}

bool operator==(Complex const & c1, Complex const & c2) {
    return c1.m_real == c2.m_real && c1.m_imag == c2.m_imag;
}

int main() {
    Complex c0, c1(20.0, -4.0), c2(3.0, 2.0);
    c0.print();
    add(c1, c2).print();
    operator+(c1, c2).print();
    (c1 + c2).print();
    subs(c1, c2).print();
    (c1 - c2).print();
    mul(c1, c2).print();
    (c1 * c2).print();
    div(c1, c2).print();
    (c1 / c2).print();
    if (c1 == c2) std::cout << "c1 == c2" << std::endl;
    else std::cout << "c1 != c2" << std::endl;
    return 0;
}
