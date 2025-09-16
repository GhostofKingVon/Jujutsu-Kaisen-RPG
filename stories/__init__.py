"""
Story modules for Jujutsu Kaisen RPG

Each arc is implemented as a separate module for better organization and maintainability.
"""

from .story1_introduction import IntroductionArc
from .story2_mahito_junpei import MahitoJunpeiArc
from .story3_cursed_womb import CursedWombArc
from .story4_vs_hanami import VsHanamiArc
from .story5_origin_obedience import OriginObedienceArc
from .story6_shibuya_incident import ShibuyaIncidentArc
from .story7_itadori_past import ItadoriPastArc
from .story8_perfect_preparation import PerfectPreparationArc
from .story9_culling_game import CullingGameArc
from .story10_final_arc import FinalArc

# Registry of all story arcs
STORY_ARCS = {
    1: IntroductionArc,
    2: MahitoJunpeiArc,
    3: CursedWombArc,
    4: VsHanamiArc,
    5: OriginObedienceArc,
    6: ShibuyaIncidentArc,
    7: ItadoriPastArc,
    8: PerfectPreparationArc,
    9: CullingGameArc,
    10: FinalArc
}

__all__ = [
    'IntroductionArc', 'MahitoJunpeiArc', 'CursedWombArc', 'VsHanamiArc',
    'OriginObedienceArc', 'ShibuyaIncidentArc', 'ItadoriPastArc',
    'PerfectPreparationArc', 'CullingGameArc', 'FinalArc', 'STORY_ARCS'
]