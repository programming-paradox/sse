import time 
from django.http import StreamingHttpResponse

def streaming_sse_view(request):
    def event_stream():
        data = [
            "This is the first part of the dummy data",
            "Second part of dummy data comes here",
            "And this is the last chunk of data"
        ]

        for chunk in data:
            yield f"data: {chunk}\n\n"
            time.sleep(1)  # Sends a new chunk every second
        
        # Signal end of data transmission
        yield "data: [END]\n\n"

    response = StreamingHttpResponse(event_stream(), content_type="text/event-stream")
    response['Cache-Control'] = 'no-cache'
    return response

