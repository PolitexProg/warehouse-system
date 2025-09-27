# services.py
from .models import Product, ProductMaterial, Warehouse

def calculate_materials(request_data):
    product_codes = [str(item['product_code']).zfill(6) for item in request_data]
    products = {p.product_code: p for p in Product.objects.filter(product_code__in=product_codes)}
    all_warehouses = Warehouse.objects.select_related('material').order_by('id')


    virtual_warehouses = []
    for wh in all_warehouses:
        virtual_warehouses.append({
            'id': wh.id,
            'material_id': wh.material.id,
            'available': wh.remainder,     
            'price': wh.price,
            'material_name': wh.material.material_name
        })

    result = []

    for item in request_data:
        code = str(item['product_code']).zfill(6)
        product_qty = item['quantity']

        if code not in products:
            continue  


        product = products[code]
        product_materials_result = []
        for pm in ProductMaterial.objects.filter(product=product).select_related('material'):
            total_needed = product_qty * pm.quantity  
            remaining = total_needed
            for batch in virtual_warehouses:
                if batch['material_id'] != pm.material.id:
                    continue


                if batch['available'] <= 0:
                    continue
                take = min(batch['available'], remaining)
                product_materials_result.append({
                    "warehouse_id": batch['id'],
                    "material_name": batch['material_name'],
                    "qty": take,
                    "price": batch['price']
                })

            
                batch['available'] -= take
                remaining -= take
                if remaining <= 0:
                    break
            if remaining > 0:
                product_materials_result.append({
                    "warehouse_id": None,
                    "material_name": pm.material.material_name,
                    "qty": remaining,
                    "price": None
                })

        result.append({
            "product_name": product.product_name,
            "product_qty": product_qty,
            "product_materials": product_materials_result
        })

    return {"result": result}