const API_URL = "/api/pedidos/mesero/";
const container = document.getElementById("mesas-container");
const token = localStorage.getItem("token_mesero");  // Guarda el token manualmente por ahora

function cargarPedidos() {
  fetch(API_URL, {
    headers: {
      "Authorization": `Bearer ${token}`
    }
  })
  .then(res => res.json())
  .then(data => {
    container.innerHTML = "";
    data.forEach(mesa => {
      const div = document.createElement("div");
      div.className = "mesa";
      div.innerHTML = `<h2>🪑 Mesa #${mesa.numero}</h2>`;

      mesa.pedidos.forEach(pedido => {
        const pedidoDiv = document.createElement("div");
        pedidoDiv.className = `pedido ${pedido.estado.toLowerCase()}`;
        pedidoDiv.innerHTML = `
          <p><strong>Pedido:</strong> ${pedido.id}</p>
          <p><strong>Estado:</strong> ${pedido.estado}</p>
          <button onclick="marcarEntregado(${pedido.id})">✅ Marcar como Entregado</button>
        `;
        div.appendChild(pedidoDiv);
      });

      container.appendChild(div);
    });
  });
}

function marcarEntregado(idPedido) {
  fetch(`/api/pedidos/actualizar/${idPedido}/`, {
    method: "PATCH",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${token}`
    },
    body: JSON.stringify({ estado: "ENTREGADO" })
  }).then(() => cargarPedidos());
}

setInterval(cargarPedidos, 10000); // auto-refresh
cargarPedidos();
