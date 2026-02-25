interface Knowledge {
    id: number | null,
    content: string,
    uri: string,
}

interface Question {
    id: number | null,
    question: string,
    knowledgeId: number,
    metric: Metric | null
}

interface Metric {
    //id: number | null,
    question_id: number,
    need_index: number
}

export type {Knowledge, Question, Metric}