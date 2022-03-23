from game.scripting.action import Action


class LoadAssetsAction(Action):

    def __init__(self, audio_service, video_service):
        self._audio_service = audio_service
        self._video_service = video_service

    def execute(self, cast, script, callback):
        self._audio_service.load_sounds("games/batter-my-completed/batter/assets/sounds")
        self._video_service.load_fonts("games/batter-my-completed/batter/assets/fonts")
        self._video_service.load_images("games/batter-my-completed/batter/assets/images")
        