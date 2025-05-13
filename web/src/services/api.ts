const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'
const TRANSLATION_ENPOINT = import.meta.env.VITE_API_URL || '/translate'

export async function fetchTranslation(text: string, language: string): Promise<string> {
  const url = `${API_URL}${TRANSLATION_ENPOINT}`
  const response = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text, language }),
  })

  if (!response.ok) {
    const errorData = await response.json()
    throw new Error(errorData.detail || 'Unknown error')
  }

  const data = await response.json()
  return data.translation
}
