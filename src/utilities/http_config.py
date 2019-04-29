def response_formatter(response_data, status):
    data = {
        "status": status,
        "message": "Created successfully" if status==201 else "Operation completed successfully",
        "data": response_data
    }
    return (data, status)

def response_formatter_with_header(response_data, status, header):
    data = {
        "status": status,
        "message": "Created successfully" if status==201 else "Operation completed successfully",
        "data": response_data
    }
    return (data, status, header)