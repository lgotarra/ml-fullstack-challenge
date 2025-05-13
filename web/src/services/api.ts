const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'
const TRANSLATION_ENDPOINT = import.meta.env.VITE_TRANSLATION_ENDPOINT || '/translate'

export async function fetchTranslation(text: string, language: string): Promise<string> {
  const url = `${API_URL}${TRANSLATION_ENDPOINT}`
  const response = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text, language }),
  })

  if (!response.ok) {
    const errorData = await response.json()

    let errorMessage = 'Unknown error'
    if (Array.isArray(errorData.detail)) {
      errorMessage = errorData.detail
        .map((item: any) => {
          const loc = item.loc?.join('.') || ''
          return `${loc}: ${item.msg}`
        })
        .join('\n')
    } else if (typeof errorData.detail === 'string') {
      errorMessage = errorData.detail
    }

    throw new Error(errorMessage)
  }

  const data = await response.json()
  return data.translation
}
