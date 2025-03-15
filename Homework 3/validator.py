from webargs import fields, validate

generate_students_validator = {
    "country": fields.Str(
        missing="UK"),
    "count": fields.Int(
        missing=10,
        validate=validate.Range(min=1, max=1000, min_inclusive=True, max_inclusive=True),
    ),
}


get_bitcoin_value_value_validator = {
    "currency": fields.Str(
        missing="USD",
    ),
    "count": fields.Int(
        missing=1,
        validate=validate.Range(min=1, max=100_000_000, min_inclusive=True, max_inclusive=True),
    )
}
