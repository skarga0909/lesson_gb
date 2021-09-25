class Road:
    _length_ = 20
    _width_ = 5000

    def calc_weight(self, weight=25, height=5):
        return weight * height * ob._length_ * ob._width_


ob = Road()
result = ob.calc_weight()
print(f'Масса асфальта: ', result)
