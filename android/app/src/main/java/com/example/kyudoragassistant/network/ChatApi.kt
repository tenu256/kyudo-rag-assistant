package com.example.kyudoragassistant.network

import retrofit2.http.Body
import retrofit2.http.POST

data class ChatRequest(
    val message: String
)

data class Source(
    val source: String,
    val chunk_index: Int
)

data class ChatResponse(
    val answer: String,
    val sources: List<Source>
)

interface ChatApi {

    @POST("chat")
    suspend fun chat(
        @Body request: ChatRequest
    ): ChatResponse
}