import React, { useState } from 'react'
import NoteForm from './components/NoteForm'
import Flashcards from './components/Flashcards'
import Quiz from './components/Quiz'

const App = () => {
  const [summary, setSummary] = useState(null)
  const [flashcards, setFlashcards] = useState([])
  const [questions, setQuestions] = useState([])

  return (
    <div className="App">
      <h1>Study Buddy</h1>
      <NoteForm
        setSummary={setSummary}
        setFlashcards={setFlashcards}
        setQuestions={setQuestions}
      />
      {summary && <div><h2>Summary</h2><p>{summary}</p></div>}
      {flashcards.length > 0 && <Flashcards flashcards={flashcards} />}
      {questions.length > 0 && <Quiz questions={questions} />}
    </div>
  )
}

export default App
