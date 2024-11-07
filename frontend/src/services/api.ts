const API_URL = 'http://localhost:8000'

export const submitNote = async (noteText: string) => {
    try {
        const response = await fetch(`${API_URL}/summarize`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text: noteText }),
        })
        const data = await response.json()

        const flashcardsResponse = await fetch(`${API_URL}/flashcards`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text: noteText }),
        })
        const flashcardsData = await flashcardsResponse.json()

        const quizResponse = await fetch(`${API_URL}/quiz`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text: noteText }),
        })
        const quizData = await quizResponse.json()

        return {
            summary: data.summary,
            flashcards: flashcardsData.flashcards,
            questions: quizData.questions,
        }
    } catch (error) {
        console.error('Error submitting note:', error)
        return { summary: '', flashcards: [], questions: [] }
    }
}
