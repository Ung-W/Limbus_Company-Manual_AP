# Object classes from AP that represent different types of options that you can create
from Options import Option, FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, OptionGroup, PerGameCommonOptions, OptionList, OptionSet
# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value
from typing import Type, Any


####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#
class victoryCondition(Range):
    """What floor will you be going to?"""
    display_name = "Final Floor"
    range_start = 5
    range_end = 15
    default = 5
    
class floorProgression(Choice):
    """
        How do you want floor progression to be?
        
        Open : All stages are available from the start, only one Boss check
        Runs : Runs are split by groups of 5 Stages, each ending in a Boss check
        
        The next options will determine how many sets of 5 stages (regardlesss of this choice) will be generated
    """
    display_name = "Floor Progression"
    option_open = 1
    option_runs = 2
    default = 1

class floor1(Range):
    """
        Define how many runs for Floor 1 are included.
    """
    display_name = "Floor 1 Runs"
    range_start = 1
    range_end = 5
    default = 3
    
class floor2(Range):
    """
        Define how many runs for Floor 2 are included.
    """
    display_name = "Floor 2 Runs"
    range_start = 1
    range_end = 5
    default = 3
    
class floor3(Range):
    """
        Define how many runs for Floor 3 are included.
    """
    display_name = "Floor 3 Runs"
    range_start = 1
    range_end = 5
    default = 2
    
class floor4(Range):
    """
        Define how many runs for Floor 4 are included.
    """
    display_name = "Floor 4 Runs"
    range_start = 1
    range_end = 5
    default = 2
    
class floor5(Range):
    """
        Define how many runs for Floor 5 are included.
        Ignored if this is your Final Floor. (will default to 1)
    """
    display_name = "Floor 5 Runs"
    range_start = 1
    range_end = 5
    default = 1
    
class floor6(Range):
    """
        Define how many runs for Floor 6 are included.
        Ignored if this is your Final Floor, or if your Final Floor is below.  (will default to 1)
    """
    display_name = "Floor 6 Runs"
    range_start = 1
    range_end = 5
    default = 1
    
class floor7(Range):
    """
        Define how many runs for Floor 7 are included.
        Ignored if this is your Final Floor, or if your Final Floor is below. (will default to 1)
    """
    display_name = "Floor 7 Runs"
    range_start = 1
    range_end = 5
    default = 1
    
class floor8(Range):
    """
        Define how many runs for Floor 8 are included.
        Ignored if this is your Final Floor, or if your Final Floor is below. (will default to 1)
    """
    display_name = "Floor 8 Runs"
    range_start = 1
    range_end = 5
    default = 1
    
class floor9(Range):
    """
        Define how many runs for Floor 9 are included.
        Ignored if this is your Final Floor, or if your Final Floor is below. (will default to 1)
    """
    display_name = "Floor 9 Runs"
    range_start = 1
    range_end = 5
    default = 1
    
class floor10(Range):
    """
        Define how many runs for Floor 10 are included.
        Ignored if this is your Final Floor, or if your Final Floor is below. (will default to 1)
    """
    display_name = "Floor 10 Runs"
    range_start = 1
    range_end = 5
    default = 1
    
class floor11(Range):
    """
        Define how many runs for Floor 11 are included.
        Ignored if this is your Final Floor, or if your Final Floor is below. (will default to 1)
    """
    display_name = "Floor 11 Runs"
    range_start = 1
    range_end = 5
    default = 1
    
class floor12(Range):
    """
        Define how many runs for Floor 12 are included.
        Ignored if this is your Final Floor, or if your Final Floor is below. (will default to 1)
    """
    display_name = "Floor 12 Runs"
    range_start = 1
    range_end = 5
    default = 1
    
class floor13(Range):
    """
        Define how many runs for Floor 13 are included.
        Ignored if this is your Final Floor, or if your Final Floor is below. (will default to 1)
    """
    display_name = "Floor 13 Runs"
    range_start = 1
    range_end = 5
    default = 1
    
class floor14(Range):
    """
        Define how many runs for Floor 14 are included.
        Ignored if this is your Final Floor, or if your Final Floor is below. (will default to 1)
    """
    display_name = "Floor 14 Runs"
    range_start = 1
    range_end = 5
    default = 1
    
class floor15(Range):
    """
        Define how many runs for Floor 15 are included.
        Ignored if this is your Final Floor, or if your Final Floor is below. (will default to 1)
    """
    display_name = "Floor 15 Runs"
    range_start = 1
    range_end = 5
    default = 1
    
class sinnerOption(OptionSet):
    """
        Toggle Sinners to be included in the pool.
        
        Note: You have a different number of minimum Sinners to be togggled on depending on your Victory Condition or your seed will NOT generate (unbeatable)
        - Floor 5+ : 3 Sinners minimum
        - Floor 8+ : 7 Sinners minimum
        - Floor 13+ : All Sinners must be included
            
        Possible values are : "Yi Sang", "Faust", "Don Quixote", "Ryoshu", "Meursault", "Honglu", "Heathcliff", "Ishmael", "Rodion", "Sinclair", "Outis", "Gregor"
    """
    display_name = "Sinners Included"
    valid_keys = ["Yi Sang", "Faust", "Don Quixote", "Ryoshu", "Meursault", "Honglu", "Heathcliff", "Ishmael", "Rodion", "Sinclair", "Outis", "Gregor"]
    default = ["Yi Sang", "Faust", "Don Quixote", "Ryoshu", "Meursault", "Honglu", "Heathcliff", "Ishmael", "Rodion", "Sinclair", "Outis", "Gregor"]
    
class sinnerStart(Choice):
    """
        Which Sinner do you start with ?
        If not random, make sure the Sinner you selected is Enabled in sinner_included
    """
    display_name = "Starting Sinner"
    option_random_sinner = 12
    option_yi_sang = 0
    option_faust = 1
    option_don_quixote = 2
    option_ryoshu = 3
    option_meursault = 4
    option_honglu = 5
    option_heathcliff = 6
    option_ishmael = 7
    option_rodion = 8
    option_sinclair = 9
    option_outis = 10
    option_gregor = 11
    default = 12
    
class sinOption(OptionSet):
    """
        Toggle Sins to be included in the pool.
            
        Possible values are : "Burn", "Bleed", "Tremor", "Rupture", "Sinking", "Poise", "Charge"
    """
    display_name = "Sins Included"
    valid_keys = ["Burn", "Bleed", "Tremor", "Rupture", "Sinking", "Poise", "Charge"]
    default = ["Burn", "Bleed", "Tremor", "Rupture", "Sinking", "Poise", "Charge"]
    
class sinStart(Choice):
    """
        Which Sin do you start with ?
        If not random, make sure the Sin you selected is Enabled in sin_included
    """
    display_name = "Starting Sin"
    option_random_sin = 7
    option_burn = 0
    option_bleed = 1
    option_tremor = 2
    option_rupture = 3
    option_sinking = 4
    option_poise = 5
    option_charge = 6
    default = 7
    
class startExclude(OptionList):
    """
        Define IDs of Sinners to be excluded from the starting pool.
        This makes it so you don't start with a Sin/Sinner combo that is unavailable to you.
        
        These Combos are excluded by default since there are no IDs that match them :
        Yi Sang: Charge | Faust: Poise | Don Quixote: Burn, Sinking, Charge
        Ryoshu: Sinking | Meursault: Charge | Honglu: Charge
        Heathcliff: Burn | Ishmael: Rupture, Sinking, Charge | Rodion: Charge
        Sinclair: Sinking, Poise, Charge | Outis: Charge | Gregor: Tremor, Poise, Charge
            
        Syntax must be "Sinner / Sin" in quotes.
        Exemple : "Yi Sang / Tremor" if you don't have a Tremor ID for Yi Sang
        
        Spelling for Sinners : "Yi Sang", "Faust", "Don Quixote",
        "Ryoshu", "Meursault", "Honglu", "Heathcliff", "Ishmael",
        "Rodion", "Sinclair", "Outis", "Gregor"
        Spelling for Sins : "Burn", "Bleed", "Tremor",
        "Rupture", "Sinking", "Poise", "Charge"
    """
    display_name = "Excluded from Starting Combo"
    default = []


# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]:
    options["victory_condition"] = victoryCondition
    options["floor_progression"] = floorProgression
    options["floor_1"] = floor1
    options["floor_2"] = floor2
    options["floor_3"] = floor3
    options["floor_4"] = floor4
    options["floor_5"] = floor5
    options["floor_6"] = floor6
    options["floor_7"] = floor7
    options["floor_8"] = floor8
    options["floor_9"] = floor9
    options["floor_10"] = floor10
    options["floor_11"] = floor11
    options["floor_12"] = floor12
    options["floor_13"] = floor13
    options["floor_14"] = floor14
    options["floor_15"] = floor15
    options["sinner_included"] = sinnerOption
    options["sinner_start"] = sinnerStart
    options["sin_included"] = sinOption
    options["sin_start"] = sinStart
    options["id_start_exclude"] = startExclude
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: Type[PerGameCommonOptions]):
    # To access a modifiable version of options check the dict in options.type_hints
    # For example if you want to change DLC_enabled's display name you would do:
    # options.type_hints["DLC_enabled"].display_name = "New Display Name"

    #  Here's an example on how to add your aliases to the generated goal
    # options.type_hints['goal'].aliases.update({"example": 0, "second_alias": 1})
    # options.type_hints['goal'].options.update({"example": 0, "second_alias": 1})  #for an alias to be valid it must also be in options

    pass

# Use this Hook if you want to add your Option to an Option group (existing or not)
def before_option_groups_created(groups: dict[str, list[Type[Option[Any]]]]) -> dict[str, list[Type[Option[Any]]]]:
    # Uses the format groups['GroupName'] = [TotalCharactersToWinWith]
    groups['Progression'] = [victoryCondition, floorProgression, floor1, floor2, floor3, floor4, floor5, floor6, floor7, floor8, floor9, floor10, floor11, floor12, floor13, floor14, floor15]
    groups['Identities'] = [sinnerOption, sinnerStart, sinOption, sinStart, startExclude]
    return groups

def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]:
    return groups
