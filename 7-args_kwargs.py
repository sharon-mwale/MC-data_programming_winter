if __name__ == "__main__":
    def variable_arguments_demo(arg1, *args, kwarg1="default_kwarg", **kwargs):
        print("arg1:", arg1)
        print("Additional args:", args)
        print("kwarg1:", kwarg1)
        print("Additional kwargs:", kwargs)

    variable_arguments_demo("Hello", "World", kwarg2="ExtraValue")
