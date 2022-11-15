from cerberus import Validator

def get_pagination_validator(request: any):
    query_param_validator = Validator({
        "page": {
            "type": "string",
            "allowed": ["1", "2", "3", "4"],
            "required": True
        }
    })

    response = query_param_validator.validate(request.query_params)

    if not response:
        raise Exception(query_param_validator.errors)
