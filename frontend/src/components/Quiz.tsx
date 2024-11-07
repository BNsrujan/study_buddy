interface Question {
    question: string
    answer: string
}

interface Props {
    questions: Question[]
}

const Quiz: React.FC<Props> = ({ questions }) => {
    return (
        <div>
            <h3>Quiz</h3>
            <ul>
                {questions.map((q, index) => (
                    <li key={index}>
                        <strong>{q.question}</strong>
                        <p>Answer: {q.answer}</p>
                    </li>
                ))}
            </ul>
        </div>
    )
}

export default Quiz
