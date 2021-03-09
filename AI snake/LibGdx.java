import java.util.ArrayList;

enum SoldierType {
    LIGHT, DARK;

    public boolean isLight() {
        return this == LIGHT;
    }

    public boolean isLDark() {
        return this == DARK;
    }
}

abstract class Soldier {
    int health;
    int damage;
    String name;
    String weapon;
    int armor;
    SoldierType type = SoldierType.LIGHT;
    Soldier(String name, int health, int damage, int armor) {
        this.name = name;
        this.health = health;
        this.damage = damage;
        this.armor = armor;
    }

    Soldier() {
    }

    Soldier(String name) {
        this.name = name;
    }

    public int getHealth() {
        return health;
    }

    public void setHealth(int health) {
        this.health = health;
    }

    public void attack(Soldier s) {
        s.getAttack(this);
    }

    public void getAttack(Soldier s) {
        int percent = (int)(s.getDamage() * 0.3);
        if(this.type == SoldierType.LIGHT && s.type == SoldierType.DARK){
        reduceHp(s.damage - percent- armor);
        }else if (s.type == SoldierType.LIGHT && this.type == SoldierType.DARK){
            reduceHp(s.damage + percent- armor);
        }
    }

    public void reduceHp(int amount) {
        this.health -= amount;
        if (this.health < 0) {
            this.health = 0;
        }
    }

    public int getDamage() {
        return damage;
    }
}

class Pikeman extends Soldier {
    Pikeman(String name) {
        super(name);
        damage = 50;
        health = 150;
        armor = 5;
    }

    Pikeman(String name, int health, int damage, int armor) {
        super(name, health, damage, armor);
    }

    void increaseAttack() {
        damage = damage * 11 / 10;
    }

    public void attack(Soldier s) {
        increaseAttack();
        super.attack(s);
    }
}

class Archer extends Soldier {
    int timesOfAttack = 2;
    int arrowCount = 4;
    boolean skipTurn = false;
    Archer(String name) {
        super(name);
        health = 80;
        damage = 40;
        armor = 0;
        type = SoldierType.DARK;

    }

    Archer(String name, int health, int damage, int armor) {
        super(name, health, damage, armor);
    }

    void setTimesOfAttack(int times) {
        timesOfAttack = times;
    }

    public void attack(Soldier s) {
        for (int i = 0; i < timesOfAttack; i++) {
            if (arrowCount > 0 && !skipTurn) {
                super.attack(s);
                arrowCount--;
            }
        }
        if (arrowCount == 0) {
            reload();
        }
        if (!skipTurn) {
            System.out.println("Archer skip this turn");
        }
        if (skipTurn) {
            skipTurn = false;
        }
    }

    public void reload() {
        arrowCount = 4;
        skipTurn = true;
    }

    public void setArrowCount(int amount) {
        arrowCount = amount;
    }
}

class Tanker extends Soldier {
    Tanker(String name) {
        super(name);
        health = 300;
        damage = 10;
        armor = 20;
    }

    Tanker(String name, int health, int damage, int armor) {
        super(name, health, damage, armor);
    }

}

class Healer extends Soldier {
    int maxReceiveDamage = 30;
    int turnToHeal = 2;

    Healer(String name) {
        super(name);
        health = 120;
        damage = 25;
        armor = 0;
    }

    Healer(String name, int health, int damage, int armor) {
        super(name, health, damage, armor);
    }

    public void healSelf(int healheal) {
        health += healheal;
    }

    public void getAttack(Soldier s) {
        if (s.damage - armor > maxReceiveDamage) {
            reduceHp(maxReceiveDamage);
        } else {
            super.reduceHp(s.damage - armor);
        }
    }
}

public class LibGdx {

    public static void main(String[] args) {
        ArrayList<Soldier> army = new ArrayList<>();

        for (int i = 0; i < 4; i++) {
            for (int j = i; j < 4; j++) {
                if (i == j) {
                    continue;
                }
                army.clear();
                Soldier archer = new Archer("archer");
                army.add(archer);
                Soldier healer = new Healer("healer");
                army.add(healer);
                Soldier tanker = new Tanker("tanker");
                army.add(tanker);
                Soldier pikeman = new Pikeman("pikeman");
                army.add(pikeman);
                while (army.get(i).getHealth() > 0 && army.get(j).getHealth() > 0) {

                    System.out.println("Hp " + army.get(i).getClass().getSimpleName() + army.get(i).getHealth());
                    System.out.println("Hp " + army.get(j).getClass().getSimpleName() + army.get(j).getHealth());

                    System.out.println("Damage " + army.get(i).getClass().getSimpleName() + army.get(i).getDamage());
                    System.out.println("Damage " + army.get(j).getClass().getSimpleName() + army.get(j).getDamage());
                    army.get(i).attack(army.get(j));
                    army.get(j).attack(army.get(i));
                    if (army.get(i).getHealth() <= 0) {
                        System.out.println(army.get(j).getClass().getSimpleName() + "Won");
                    } else if (army.get(j).getHealth() <= 0) {
                        System.out.println(army.get(i).getClass().getSimpleName() + "Won");
                    }
                    System.out.println("");
                }
                System.out.println("####################################################################");

            }
        }

    }

}
