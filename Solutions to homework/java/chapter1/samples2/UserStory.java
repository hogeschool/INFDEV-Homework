package chapter1.samples2;

public class UserStory {
    int hours;
    String description;

    public UserStory() {
    }

    public UserStory(int hours, String description) {
        this.hours = hours;
        this.description = description;
    }

    public int getHours() {
        return hours;
    }

    public void setHours(int hours) {
        this.hours = hours;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    @Override
    public String toString(){
        return getDescription() + ": " + getHours();
    }

    public static void main(String[] args) {
        UserStory us1 = new UserStory(10, "Als gebruiker wil ik inloggen!");
        UserStory us2 = new UserStory(10, "Als gebruiker wil ik inloggen!");

        System.out.println(us1 == us2);
    }

}
