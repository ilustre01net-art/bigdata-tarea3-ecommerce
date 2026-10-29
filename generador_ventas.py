cat << 'EOF' > generador_ventas.py
import csv
import random
from datetime import datetime, timedelta

print("Generando conjunto de datos de transacciones comerciales...")
with open("ventas_ecommerce_batch.csv", mode="w", newline="") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["transaction_id", "customer_id", "product_category", "amount", "payment_method", "timestamp"])
    
    categorias = ["Electronica", "Ropa", "Hogar", "Deportes", "Juguetes"]
    pagos = ["Tarjeta_Credito", "PSE", "Efecty", "Transferencia"]
    
    start_time = datetime(2026, 10, 1, 8, 0, 0)
    for i in range(15000):
        trans_id = 1000 + i
        cust_id = random.randint(500, 800)
        categoria = random.choice(categorias)
        amount = round(random.uniform(10.0, 2500.0), 2)
        if i % 300 == 0:
            amount = -50.0  # Dato erróneo para limpieza
        
        metodo = random.choice(pagos)
        timestamp = (start_time + timedelta(minutes=random.randint(1, 43200))).strftime("%Y-%m-%d %H:%M:%S")
        
        writer.writerow([trans_id, cust_id, categoria, amount, metodo, timestamp])

print("¡Archivo 'ventas_ecommerce_batch.csv' con 15,000 registros creado con éxito!")
EOF
