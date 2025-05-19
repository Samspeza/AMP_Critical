import React, { useEffect, useState } from "react";
import axios from "axios";

export default function RegioesCriticas() {
  const [dados, setDados] = useState([]);

  useEffect(() => {
    axios.get("/regioes_criticas.json")
      .then((res) => setDados(res.data))
      .catch((err) => console.error("Erro ao carregar dados críticos:", err));
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Visualização de Regiões Críticas</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {dados.map((item, idx) => (
          <div key={idx} className="border p-4 rounded-xl shadow-md bg-white">
            <p><strong>Feature 1:</strong> {item.feature1.toFixed(2)}</p>
            <p><strong>Feature 2:</strong> {item.feature2.toFixed(2)}</p>
            <p><strong>Erro:</strong> {item.residual.toFixed(2)}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
