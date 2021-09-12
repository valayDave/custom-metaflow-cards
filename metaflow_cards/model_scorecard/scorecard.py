from metaflow.plugins.card_modules.card import MetaflowCard

class ScoreCard(MetaflowCard):
    name='custom_score_card'
    
    def render(self, task):
        mustache = self._get_mustache()
        TEMPLATE = f"""
        THIS IS A CUSTOM SCORE CARD
        """
        return mustache.render(TEMPLATE)
        