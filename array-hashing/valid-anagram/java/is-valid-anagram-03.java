public static boolean isAnagram(String s, String t) {
        char sortS[] = s.toCharArray();
        Arrays.sort(sortS);

        char sortT[] = t.toCharArray();
        Arrays.sort(sortT);

        return Arrays.equals(sortS, sortT);
    }