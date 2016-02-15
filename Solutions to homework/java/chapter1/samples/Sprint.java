package chapter1.samples;

public class Sprint {
    UserStory[] userStories;

    public static void main(String[] args) {
        Sprint sprint = new Sprint();
        sprint.userStories = new UserStory[3];

        UserStory us = new UserStory();
        us.setDescription("Als gebruiker wil ik kaas eten. veel!");
        us.setHours(10);
        sprint.userStories[0] = us;

        us = new UserStory();
        us.setDescription("Als gebruiker wil ik worst eten. veel!");
        us.setHours(5);
        sprint.userStories[1] = us;

        us = new UserStory();
        us.setDescription("Als gebruiker wil ik melk eten. :( hoe dan?!");
        us.setHours(1);
        sprint.userStories[2] = us;

        //oude stijl
        for(int i = 0; i < sprint.userStories.length; i++){
            //System.out.println(userStories[i]);
        }



    }

    public void totalHours(){
        int sum = 0;
        //nieuwe stijl for i in [1,2,4,5]
        for(UserStory userStory: userStories){
            if (userStory != null) {
//                System.out.println(userStory);
                sum += userStory.getHours();
            }
        }

        System.out.println(sum);
    }
}
