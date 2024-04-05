class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else: 
            self.carrito = carrito

    def add(self, product): #agregar
        id = str(product.id)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "producto_id" : product.id,
                "nombre" : product.name,
                "acumulado" : product.price,
                "cantidad" : 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += product.price
        self.save_cart()

    def save_cart(self): #guardar carrito
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def delete(self, product): #eliminar
        id = str(product.id)
        if id in self.carrito:
            del self.carrito[id]
            self.save_cart()
    
    def subtract(self,product): #restar
        id = str(product.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= product.price
            if self.carrito[id]["cantidad"] <= 0 : self.delete(product)
            self.save_cart()

    def clear(self): #limpiar
        self.session["carrito"] = {}
        self.session.modified = True
    