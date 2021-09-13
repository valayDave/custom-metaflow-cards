from metaflow.plugins.card_modules.card import MetaflowCard

class ScoreCard(MetaflowCard):
    name='custom_score_card'

    type = 'task'
    
    def __init__(self,footer=False) -> None:
        self._footer = footer
    
    def render(self, task):
        mustache = self._get_mustache()
        TEMPLATE = """
        %s
        """%(task.id)
        if self._footer: 
            TEMPLATE = """
        %s
        With Footer
        """%(task.id)
            
        return mustache.render(TEMPLATE)
        