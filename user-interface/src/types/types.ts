interface Knowledge {
    id: number | null,
    content: string,
    uri: string,
}

interface Question {
    id: number | null,
    question: string,
    knowledgId: number,
    metric: Metric | null
}

interface Metric {
    id: number | null,
    questionId: number,
    needIndex: number
}

export type {Knowledge, Question, Metric}