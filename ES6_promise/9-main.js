export default function guardrail(mathFunction) {
  const g = [];

  try {
    const result = mathFunction();
    g.push(result);
  } catch (error) {
    g.push(`Error: ${error.message}`);
  } finally {
    g.push('Guardrail was processed');
  }

  return g;
}
