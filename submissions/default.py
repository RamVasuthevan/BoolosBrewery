"""
Sample strategy, to demonstrate how to implement one.
"""

from strats import *

class Strategy(Default):
    """
    The strategy must be implemented in a class called "Strategy", which derives from the appropriate difficulty level.
    Difficulty levels: Easy, Default, Hard.
    """

    # The Solver class must have a static parameter `engg_question_limit`, which specifies an upper bound for how many
    # questions you may end up asking the engineer.
    # You can go under this number, but you can't go over, or the game will crash.
    # Note: this quantity determines submission runtime (the relationship is exponential), so try to use a tight upper
    # bound if possible!
    # In our case, since we're solving the Easy variant of the puzzle, engg_question_limit can be zero
    # (there are no engineers present).
    engg_question_limit = 1

    def solve(game):
        """
        This is the entrypoint for solving the puzzle.
        When invoked, a game instance is already running.
        Invoke "self.ask" to pass a Question instance to the game.
        The return value will be a Response instance.

        When you believe you have solved the puzzle (in `question_limit` or fewer), call "self.guess".
        This function takes an assignment of Alice, Bob[, Charlie[, Dan]] to Field instances.
        """

        alice_says_charlie_studies_engineering =  game.get_response(Alice.ask(Foo.equals(Charlie.studies(Engg)))) is Foo

        if alice_says_charlie_studies_engineering:
            bob_says_charlie_studies_engineering = game.get_response(Bob.ask(Foo.equals(Charlie.studies(Engg)))) is Foo

            if bob_says_charlie_studies_engineering:
                game.guess[Charlie] = Engg

                alice_studies_math =  game.get_response(Alice.ask(Foo.equals(Alice.studies(Math)))) is Foo
                game.guess[Alice] = Math if alice_studies_math else Phys
                game.guess[Bob] = Phys if alice_studies_math else Math

            else:
                game.guess[Alice] = Engg

                bob_studies_math =  game.get_response(Bob.ask(Foo.equals(Bob.studies(Math)))) is Foo
                game.guess[Bob] = Math if bob_studies_math else Phys
                game.guess[Charlie] = Phys if bob_studies_math else Math
        else:
            carlie_says_alice_studies_engineering = game.get_response(Charlie.ask(Foo.equals(Alice.studies(Engg)))) is Foo
            if carlie_says_alice_studies_engineering:
                game.guess[Alice] = Engg

                bob_studies_math =  game.get_response(Bob.ask(Foo.equals(Bob.studies(Math)))) is Foo
                game.guess[Bob] = Math if bob_studies_math else Phys
                game.guess[Charlie] = Phys if bob_studies_math else Math

            else:
                game.guess[Bob] = Engg

                alice_studies_math =  game.get_response(Alice.ask(Foo.equals(Alice.studies(Math)))) is Foo
                game.guess[Alice] = Math if alice_studies_math else Phys
                game.guess[Charlie] = Phys if alice_studies_math else Math