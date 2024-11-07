interface Flashcard {
    term: string
    definition: string
}

interface Props {
    flashcards: Flashcard[]
}

const Flashcards: React.FC<Props> = ({ flashcards }) => {
    return (
        <div>
            <h3>Flashcards</h3>
            <ul>
                {flashcards.map((flashcard, index) => (
                    <li key={index}>
                        <strong>{flashcard.term}</strong>: {flashcard.definition}
                    </li>
                ))}
            </ul>
        </div>
    )
}

export default Flashcards
