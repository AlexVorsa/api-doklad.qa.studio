"""
Schema for trainer
"""
from voluptuous import Schema, PREVENT_EXTRA

valid_trainer = Schema(
    {
        "city": str,
        "get_history_battle":str,
        "id":str,
        "level":str,
        "photo":str,
        "pokemons":list,
        "pokemons_alive":list,
        "pokemons_in_pokeballs":list,
        "trainer_name": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

error_trainer = Schema(
    {
        "message":str,
        "status":str
    },
    extra=PREVENT_EXTRA,
    required=True
)

update_trainer = Schema(
    {
        "id":str,
        "message":str
    },
    extra=PREVENT_EXTRA,
    required=True
)
