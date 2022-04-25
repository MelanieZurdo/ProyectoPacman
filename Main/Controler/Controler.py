from Main.Model.LevelFactory import LevelFactory


class Controler:
    def main(self):
        level_factory=LevelFactory()
        level_one=level_factory.get_level_one()
        print(level_one.board)

if __name__ == '__main__':
    controler=Controler()
    controler.main()