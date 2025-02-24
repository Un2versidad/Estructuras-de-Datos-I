const problems = [
  {
    title: "Suma Máxima de Subarreglo",
    description: "Encuentra el subarreglo con la suma más grande y devuelve dicha suma.",
    points: 5,
    githubUrl: "https://github.com/Un2versidad/Estructuras-de-Datos-I/tree/main/Examen%20Parcial%201-A%20(Individual)/Problema%201",
    rawUrl: "https://raw.githubusercontent.com/Un2versidad/Estructuras-de-Datos-I/refs/heads/main/Examen%20Parcial%201-A%20(Individual)/Problema%201/P1_Problema1.py"
  },
  {
    title: "Ordenamiento por Inserción",
    description: "Implementa el algoritmo de Ordenamiento por Inserción y determina su complejidad temporal.",
    points: 5,
    githubUrl: "https://github.com/Un2versidad/Estructuras-de-Datos-I/tree/main/Examen%20Parcial%201-A%20(Individual)/Problema%202",
    rawUrl: "https://raw.githubusercontent.com/Un2versidad/Estructuras-de-Datos-I/refs/heads/main/Examen%20Parcial%201-A%20(Individual)/Problema%202/P1_Problema2.py"
  },
  {
    title: "Operaciones con Conjuntos",
    description: "Implementa funciones para unión, intersección y diferencia de conjuntos.",
    points: 5,
    githubUrl: "https://github.com/Un2versidad/Estructuras-de-Datos-I/tree/main/Examen%20Parcial%201-A%20(Individual)/Problema%203",
    rawUrl: "https://raw.githubusercontent.com/Un2versidad/Estructuras-de-Datos-I/refs/heads/main/Examen%20Parcial%201-A%20(Individual)/Problema%203/P1_Problema3.py"
  },
  {
    title: "Subconjuntos",
    description: "Determina si un conjunto es subconjunto de otro.",
    points: 5,
    githubUrl: "https://github.com/Un2versidad/Estructuras-de-Datos-I/tree/main/Examen%20Parcial%201-A%20(Individual)/Problema%204",
    rawUrl: "https://raw.githubusercontent.com/Un2versidad/Estructuras-de-Datos-I/refs/heads/main/Examen%20Parcial%201-A%20(Individual)/Problema%204/P1_Problema4.py"
  },
  {
    title: "Registro de Estudiantes",
    description: "Encuentra el estudiante con la calificación más alta.",
    points: 5,
    githubUrl: "https://github.com/Un2versidad/Estructuras-de-Datos-I/tree/main/Examen%20Parcial%201-A%20(Individual)/Problema%205",
    rawUrl: "https://raw.githubusercontent.com/Un2versidad/Estructuras-de-Datos-I/refs/heads/main/Examen%20Parcial%201-A%20(Individual)/Problema%205/P1_Problema5.py"
  },
  {
    title: "Sistema de Inventario",
    description: "Implementa un sistema CRUD para manejo de inventario.",
    points: 5,
    githubUrl: "https://github.com/Un2versidad/Estructuras-de-Datos-I/tree/main/Examen%20Parcial%201-A%20(Individual)/Problema%206",
    rawUrl: "https://raw.githubusercontent.com/Un2versidad/Estructuras-de-Datos-I/refs/heads/main/Examen%20Parcial%201-A%20(Individual)/Problema%206/P1_Problema6.py"
  },
  {
    title: "Lista Enlazada Simple",
    description: "Implementa operaciones básicas de una lista enlazada simple.",
    points: 5,
    githubUrl: "https://github.com/Un2versidad/Estructuras-de-Datos-I/tree/main/Examen%20Parcial%201-A%20(Individual)/Problema%207",
    rawUrl: "https://raw.githubusercontent.com/Un2versidad/Estructuras-de-Datos-I/refs/heads/main/Examen%20Parcial%201-A%20(Individual)/Problema%207/P1_Problema7.py"
  },
  {
    title: "Lista Doblemente Enlazada",
    description: "Invierte el orden de una lista doblemente enlazada.",
    points: 5,
    githubUrl: "https://github.com/Un2versidad/Estructuras-de-Datos-I/tree/main/Examen%20Parcial%201-A%20(Individual)/Problema%208",
    rawUrl: "https://raw.githubusercontent.com/Un2versidad/Estructuras-de-Datos-I/refs/heads/main/Examen%20Parcial%201-A%20(Individual)/Problema%208/P1_Problema8.py"
  },
  {
    title: "Implementación de Pila",
    description: "Implementa una pila con operaciones básicas usando un arreglo dinámico.",
    points: 5,
    githubUrl: "https://github.com/Un2versidad/Estructuras-de-Datos-I/tree/main/Examen%20Parcial%201-A%20(Individual)/Problema%209",
    rawUrl: "https://raw.githubusercontent.com/Un2versidad/Estructuras-de-Datos-I/refs/heads/main/Examen%20Parcial%201-A%20(Individual)/Problema%209/P1_Problema9.py"
  },
  {
    title: "Expresiones Balanceadas",
    description: "Verifica el balance de paréntesis, corchetes y llaves en una expresión.",
    points: 5,
    githubUrl: "https://github.com/Un2versidad/Estructuras-de-Datos-I/tree/main/Examen%20Parcial%201-A%20(Individual)/Problema%2010",
    rawUrl: "https://raw.githubusercontent.com/Un2versidad/Estructuras-de-Datos-I/refs/heads/main/Examen%20Parcial%201-A%20(Individual)/Problema%2010/P1_Problema10.py"
  },
  {
    title: "Implementación de Cola",
    description: "Implementa una cola con operaciones básicas usando arreglos.",
    points: 5,
    githubUrl: "https://github.com/Un2versidad/Estructuras-de-Datos-I/tree/main/Examen%20Parcial%201-A%20(Individual)/Problema%2011",
    rawUrl: "https://raw.githubusercontent.com/Un2versidad/Estructuras-de-Datos-I/refs/heads/main/Examen%20Parcial%201-A%20(Individual)/Problema%2011/P1_Problema11.py"
  },
  {
    title: "Sistema de Atención",
    description: "Simula un sistema FIFO de atención en una tienda.",
    points: 5,
    githubUrl: "https://github.com/Un2versidad/Estructuras-de-Datos-I/tree/main/Examen%20Parcial%201-A%20(Individual)/Problema%2012",
    rawUrl: "https://raw.githubusercontent.com/Un2versidad/Estructuras-de-Datos-I/refs/heads/main/Examen%20Parcial%201-A%20(Individual)/Problema%2012/P1_Problema12.py"
  },
  {
    title: "Cola con Dos Pilas",
    description: "Implementa una cola utilizando dos pilas.",
    points: 5,
    githubUrl: "https://github.com/Un2versidad/Estructuras-de-Datos-I/tree/main/Examen%20Parcial%201-A%20(Individual)/Problema%2013",
    rawUrl: "https://raw.githubusercontent.com/Un2versidad/Estructuras-de-Datos-I/refs/heads/main/Examen%20Parcial%201-A%20(Individual)/Problema%2013/P1_Problema13.py"
  },
  {
    title: "Detección de Ciclos",
    description: "Implementa el algoritmo de Floyd para detectar ciclos en una lista enlazada.",
    points: 15,
    githubUrl: "https://github.com/Un2versidad/Estructuras-de-Datos-I/tree/main/Examen%20Parcial%201-A%20(Individual)/Problema%2014",
    rawUrl: "https://raw.githubusercontent.com/Un2versidad/Estructuras-de-Datos-I/refs/heads/main/Examen%20Parcial%201-A%20(Individual)/Problema%2014/P1_Problema14.py"
  },
  {
    title: "Sistema de Entrega de Pedidos",
    description: "Implementa un sistema de gestión de pedidos con prioridades.",
    points: 20,
    githubUrl: "https://github.com/Un2versidad/Estructuras-de-Datos-I/tree/main/Examen%20Parcial%201-A%20(Individual)/Problema%2015",
    rawUrl: "https://raw.githubusercontent.com/Un2versidad/Estructuras-de-Datos-I/refs/heads/main/Examen%20Parcial%201-A%20(Individual)/Problema%2015/P1_Problema15.py"
  }
];

// Efecto de Luz Cursor
document.addEventListener('mousemove', (e) => {
  document.documentElement.style.setProperty('--cursor-x', `${e.clientX}px`);
  document.documentElement.style.setProperty('--cursor-y', `${e.clientY}px`);
});

// Crea las Cartas de los Problemas
const problemsContainer = document.getElementById('problems-container');

problems.forEach((problem, index) => {
  const card = document.createElement('div');
  card.className = 'problem-card';

  card.innerHTML = `
    <div class="problem-content">
      <div class="window-controls">
        <div class="window-control red"></div>
        <div class="window-control yellow"></div>
        <div class="window-control green"></div>
      </div>

      <div class="problem-header">
        <h2 class="problem-number">Problema ${index + 1}</h2>
        <span class="problem-points">${problem.points} puntos</span>
      </div>

      <h3 class="problem-title">${problem.title}</h3>
      <p class="problem-description">${problem.description}</p>

      <a href="${problem.githubUrl}"
        target="_blank"
        class="github-link">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/>
        </svg>
        Ver código en GitHub
      </a>

      <button class="execute-button" onclick="executeCode(${index + 1}, '${problem.rawUrl}')" id="button-${index + 1}">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <polygon points="5 3 19 12 5 21 5 3"/>
        </svg>
        Ejecutar Código
      </button>

      <div class="output-container">
        <div class="output-header">
          <span class="output-label">Salida</span>
        </div>
        <pre class="output-content" id="output-${index + 1}">📤 Esperando ejecución del código...</pre>
      </div>
    </div>
  `;

  problemsContainer.appendChild(card);
});

async function executeCode(problemNumber, rawUrl) {
  const button = document.getElementById(`button-${problemNumber}`);
  const output = document.getElementById(`output-${problemNumber}`);

  button.disabled = true;
  button.innerHTML = `
    <svg class="animate-spin" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <circle cx="12" cy="12" r="10" stroke-dasharray="32" stroke-dashoffset="32"/>
    </svg>
    Ejecutando...
  `;

  try {
    const response = await fetch(rawUrl);
    const code = await response.text();

    const result = await fetch("https://emkc.org/api/v2/piston/execute", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        language: "python",
        version: "3.10.0",
        files: [{ content: code }]
      })
    });

    const data = await result.json();
    output.textContent = data.run.output || '✨ Ejecución completada exitosamente!';
  } catch (error) {
    output.textContent = '❌ Error al ejecutar el código. Por favor, intente nuevamente.';
  }

  button.disabled = false;
  button.innerHTML = `
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <polygon points="5 3 19 12 5 21 5 3"/>
    </svg>
    Ejecutar Código
  `;
}