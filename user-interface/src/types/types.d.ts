interface KnowledgeCreate{
    content: string,
    uri: string,
}

interface Knowledge {
    id: number | null,
    content: string,
    uri: string,
    user: User
}

interface Question {
    id: number | null,
    question: string,
    knowledgeId: number,
    metric: Metric | null
    user: User
}

interface MetricCreate {
    question_id: number,
    need_index: number
}

interface User {
    username: string,
    token: string
}

export type {KnowledgeCreate, Knowledge, Question, MetricCreate}