from ui_elements.collection_loader import CollectionLoader

if __name__ == "__main__":
    while True:
        collection_load = CollectionLoader()
        collection_load.minsize(400, 400)
        collection_load.mainloop()

        if not collection_load.should_restart:
            break