def total_carrito(request):
    total = 0
    if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                total += int(value["acumulado"])   
    
    #total=100
    return {"total_carrito": total}