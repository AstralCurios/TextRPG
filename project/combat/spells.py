# manages spells for characters

def cast_fireball(caster, target, cost, dmg):
    if caster.mana < cost:
        raise Exception(f"{caster.name} cannot cast fireball")
    caster.mana -= cost
    reduced = max(0, dmg - getattr(target, "_stamina", 0))
    target.take_damage(reduced)