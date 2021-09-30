from metaflow.plugins.card_modules.card import MetaflowCard

class ScoreCard(MetaflowCard):
    type='custom_score_card'

    scope = 'task'
    
    def __init__(self,options=dict(footer=False)) -> None:
        self._footer = options['footer']
    
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
        