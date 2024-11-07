import React, { useState } from 'react'
import { submitNote } from '../services/api'

interface Props {
    setSummary: React.Dispatch<React.SetStateAction<string | null>>
    setFlashcards: React.Dispatch<React.SetStateAction<any[]>>
    setQuestions: React.Dispatch<React.SetStateAction<any[]>>
}

const NoteForm: React.FC<Props> = ({ setSummary, setFlashcards, setQuestions }) => {
    const [noteText, setNoteText] = useState<string>('')

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault()
        const response = await submitNote(noteText)
        setSummary(response.summary)
        setFlashcards(response.flashcards)
        setQuestions(response.questions)
    }

    return (
        <form onSubmit={handleSubmit}>
            <textarea
                value={noteText}
                onChange={(e) => setNoteText(e.target.value)}
                placeholder="Enter your notes here..."
            />
            <button type="submit">Submit</button>
        </form>
    )
}

export default NoteForm
