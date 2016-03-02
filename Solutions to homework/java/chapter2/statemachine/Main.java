package chapter2.statemachine;

import javafx.animation.AnimationTimer;
import javafx.application.Application;
import javafx.stage.Stage;

public class Main extends Application{
    public static void main(String[] args) {
        launch();
    }

    @Override
    public void start(Stage primaryStage) throws Exception {
        Sequence s = new Sequence(new Wait(10f), new Print("Hello World!"));
        new AnimationTimer() {
            public void handle(long currentNanoTime) {
                s.update(1f);
                try {
                    Thread.sleep(500);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }.start();
    }
}
