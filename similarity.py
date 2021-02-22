import face_recognition as fr

class similarity:

    def __init__(self):
        self.target1 = []
        self.target2 = []

    def loadAndEncode(self, image_file1, image_file2):
        image1 = fr.load_image_file(image_file1)
        image2 = fr.load_image_file(image_file2)
        self.target1 = fr.face_encodings(image1)
        self.target2 = fr.face_encodings(image2)

        return len(self.target1), len(self.target2)

    def areSimilar(self):
        tol1 = 0.6
        tol2 = 1
        m = []
        err = []
        err.append(1)
        m.append(tol1)
        result = fr.compare_faces(self.target1, self.target2[0], m)


        if result[0] == True: #sono la stessa persona
            return result, m[-1]
        else: #non sono la stessa persona aumento la tolleranza
            result[0] = True
            while err[-1] > 1e-6:

                m.append( (tol1 + tol2) / 2 )
                result = fr.compare_faces(self.target1, self.target2[0], m[-1])

                if result[0] == True: #vuol dire che una tolleranza migliore potrebbe trovarsi fra tol1 e m
                    tol2 = m[-1]
                else: #vuol dire che la tollerazna migliore potrebbe trovarsi fra m e tol2
                    tol1 = m[-1]

                err.append( abs(m[-1] - m[-2]) )

            return result, m[-1]

    def inizialize(self):
        image_file1 = input("Target Image File > ")
        image_file2 = input("Image File to compare > ")
        t1, t2 = self.loadAndEncode( image_file1, image_file2)
        print("Wait just a few seconds...")
        print(f"There are {t1} person/people in the first image and {t2} in the second one")

    def run(self):
        self.inizialize()
        result = self.areSimilar()
        return result

if __name__ == "__main__":
    x = similarity()
    result = x.run()
    print(f"Similarity index: {result[1]}")